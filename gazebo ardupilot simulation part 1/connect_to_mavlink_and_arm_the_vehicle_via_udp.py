from pymavlink import mavutil

# Create a connection to the vehicle using UDP (localhost)
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

print("Waiting for heartbeat...")
master.wait_heartbeat()
print("Connected!")

# Send command to arm the vehicle
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)

print("Vehicle is being armed...")
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print("Armed!")
