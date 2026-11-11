import math
import random
import copy

def run_simulation(rocket, wind_v=None):
    rocket = copy.deepcopy(rocket)

    if wind_v is None:
        wind_v = random.randint(-30, 30)

    t = 0
    x = 0
    h = 0
    h_max = h
    g0 = 9.806
    rho0 = 1.225
    radius = 6371000
    c = 0.3
    dt = 0.1 
    v_y = 0
    v_x = 0
    theta = math.radians(90)
    turn_rate = math.radians(0.5)
    time_data = []
    altitude_data = []
    xvelocity_data = []
    yvelocity_data = []
    nvelocity_data = []
    drag_data = []
    range_data = []
    liftoff = True
    burnout = False

    status = "timeout"

    while liftoff and t<2000:
        stage = rocket.stages[rocket.current_stage]
        if stage.fuelmass >0:
            thrust = stage.thrust
            stage.fuelmass = max(0, stage.fuelmass - stage.fuelrate*dt)

        else:
            thrust = 0

        totalmass = rocket.mass + sum(s.fuelmass for s in rocket.stages)
        rho = rho0*math.exp(-h/8500)
        drag_y = 0.5 *rho*c*rocket.area*abs(v_y)*v_y
        drag_x = 0.5*rho*c*rocket.area*((v_x - wind_v)*abs(v_x - wind_v))
        g = g0*(radius / (radius + h))**2

        Fnet_y = thrust*math.sin(theta) - totalmass*g - drag_y
        Fnet_x = thrust*math.cos(theta) - drag_x
        a_y = Fnet_y/totalmass
        a_x = Fnet_x/totalmass
        v_y += a_y*dt
        v_x += a_x*dt
        h += v_y*dt
        if h < 0:
            status = "crashed"
            break
        h_max = max(h, h_max)
        x += v_x*dt 
        v_net = math.sqrt(v_x**2 + v_y**2)

    # Not realistic. Only for testing purposes.
        
        if h > 1500 and theta > math.radians(30):
            theta = max(math.radians(30), theta - turn_rate * dt)

        t += dt
    # Stage Separation
        if stage.fuelmass <= 0:
                if len(rocket.stages) - 1 > rocket.current_stage:
                    rocket.mass -= stage.bodymass
                    rocket.current_stage += 1
                    

                else: 
                    if not burnout:
                        burnout = True

        time_data.append(t)
        altitude_data.append(h/1000)
        xvelocity_data.append(v_x)
        yvelocity_data.append(v_y)
        nvelocity_data.append(v_net)
        drag_data.append(drag_y)
        range_data.append(x)

        
        all_fuel_exhausted = all(
            s.fuelmass <= 0 for s in rocket.stages
        )

        if all_fuel_exhausted and v_y <= 0:
            status = "apogee_reached"
            break

    results = {
    "status": status,
    "max_altitude": h_max,
    "max_range": x,
    "flight_time": t,
    "wind_speed": wind_v,
    "time_data": time_data,
    "altitude_data": altitude_data,
    "xvelocity_data": xvelocity_data,
    "yvelocity_data": yvelocity_data,
    "nvelocity_data": nvelocity_data,
    "drag_data": drag_data,
    "range_data": range_data
    }

    return results
