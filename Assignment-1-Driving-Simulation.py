print("Driving Simulation")
time= int(input("Time Taken(s):"))
acc= int(input("Acceleration (m/s2):"))
dist = int(input("Distance (m):"))
maxspeed = int(acc*time)

for i in range(0,time+1):
    dist2=(acc*(i*i)/2)
    star= int(dist2/10)
    print("Duration (s):", i, end="")
    print(" Distance", "*"*star)
if (acc > 60):
    print("The person went over the speed limit.(Max speed was",maxspeed,"m/s)")

else :
    print("The person didnt go over the speed limit.(Max speed was",maxspeed,"m/s)")

if (dist2>dist) :
    print("The person reached the destination.(Reached", dist2, " m)")

else :
    print("The person didnt reach the destination.(Reached", dist2, " m)")