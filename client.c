#include <zmq.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h> 
#include <time.h>
#include <unistd.h>
#include <json-c/json.h>

int main()
{
    printf("Connecting to server...\n");
    json_object *json_obj = NULL;
    json_obj = json_object_new_array();
    void * context = zmq_ctx_new();
    // 使用 zmq.REQ 模式，做為 client 端
    void * socket = zmq_socket(context, ZMQ_REQ);
    zmq_connect(socket, "tcp://127.0.0.1:5566");
    srand(time(NULL));
    int min=20;
    int max=40;
    for(int i = 1; i < 11; i++)
    {
	int x=rand() % (max - min + 1) + min;
	int y=0;
        zmq_send(socket, &x,1,0);
        zmq_recv(socket, &y,1,0);
        json_object *tmp_obj = json_object_new_int(x);
	json_object *tmp1_obj = json_object_new_int(y);
        json_object_array_add(json_obj,tmp_obj);
        json_object_array_add(json_obj,tmp1_obj);
    }   
    int C=0;
    zmq_send(socket, &C,1,0);
    zmq_close(socket);
    zmq_ctx_destroy(context);
    json_object_to_file("location.json",json_obj);
    json_object_put(json_obj);
    return 0;
}
