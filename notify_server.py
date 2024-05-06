import bpy
import socket

SERVER_ADDRESS = "localhost"
SERVER_PORT = 5000

target_frame=113
closing_frame=300
notified_frame=set()

def notify_target_frame(scene,depsgraph):
    # Check if current frame matches the target frame
    current_frame=scene.frame_current
    if current_frame not in notified_frame:
        print(current_frame)
        if current_frame == target_frame: 
            # Create a socket and connect to the server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((SERVER_ADDRESS, SERVER_PORT))

                # Send notification message
                message = f"Frame {target_frame} reached!"
                sock.sendall(message.encode())
                print(f"Sent notification: {message}")
            if closing_frame in notified_frame:
                notified_frame.remove(closing_frame)
        if current_frame == closing_frame: 
            # Create a socket and connect to the server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((SERVER_ADDRESS, SERVER_PORT))

                # Send notification message
                message = f"Frame {closing_frame} reached!"
                sock.sendall(message.encode())
                print(f"Sent notification: {message}")
            if target_frame in notified_frame:
                notified_frame.remove(target_frame)
        notified_frame.add(current_frame)
# Register a handler to be called on frame change
bpy.app.handlers.frame_change_post.append(notify_target_frame)
