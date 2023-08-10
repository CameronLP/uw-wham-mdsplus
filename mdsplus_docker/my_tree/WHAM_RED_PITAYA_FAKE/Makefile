all: libWhamRedPitayaFakeShr.so

clean:
	rm libWhamRedPitayaFakeShr.so

libWhamRedPitayaFakeShr.so: WHAM_RED_PITAYA_FAKE.c
	gcc -fPIC -shared -o libWhamRedPitayaFakeShr.so WHAM_RED_PITAYA_FAKE.c -lm

	
