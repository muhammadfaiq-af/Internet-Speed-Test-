import speedtest
st = speedtest.Speedtest()

option = int(input("What speed do you want to test 1) Downloading 2) Uplodaing"))
if option == 1:
    print("Your Connection's Downloading Speed is : " + st.download())
if option == 2:
    print("Your Connection's Uploading Speed is : " + st.upload())
else:
    print("Enter the valid Number")