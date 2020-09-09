from speedtest import Speedtest

st = Speedtest()

print("La velocidad de descarga es: ", st.download())

print("La velocidad de subida es: ", st.upload())