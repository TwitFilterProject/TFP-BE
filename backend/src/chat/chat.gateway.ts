import {
    SubscribeMessage,
    WebSocketGateway,
    WebSocketServer,
    OnGatewayConnection,
    OnGatewayDisconnect,
    MessageBody
} from '@nestjs/websockets';
import { Server, Socket } from 'socket.io';
import axios from 'axios';

@WebSocketGateway()
export class ChatGateway implements OnGatewayConnection, OnGatewayDisconnect {
    users: string[];

    constructor() {
        this.users = [];
    }

    @WebSocketServer() server: Server;
    private clients: Socket[] = [];

    handleConnection(client: Socket) {
        this.clients.push(client);
        this.users.push(client.id)
        console.log('Client connected:', client.id);
        console.log('Current Clients', this.users);
    }

    handleDisconnect(client: Socket) {
        this.clients = this.clients.filter((c) => c.id !== client.id);
        this.users = this.users.filter((c) => c !== client.id);
        console.log('Client disconnected:', client.id);
        console.log('Current Clients', this.users);
    }

    @SubscribeMessage('chat')
    async handleMessage(@MessageBody() payload: any): Promise<void>  {
        console.log(payload.body);
        const body = payload.body;
        const {data} = await axios.post('http://127.0.0.1:5000/test', {body});
        console.log(data)
        this.server.emit('chat', {sender: payload.sender, body: data});
    }
}
  