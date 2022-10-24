CC=gcc

client:client.c
	$(CC) -o client client.c  -lzmq -ljson-c
clean:
	rm *.o
