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
    private users: {id: string, nickname: string}[] = [];

    @WebSocketServer() server: Server;
    private clients: Socket[] = [];

    handleConnection(client: Socket) {
        this.clients.push(client);
        console.log('Client connected:', client.id);
        this.server.emit("socketId", client.id)
    }

    handleDisconnect(client: Socket) {
        this.clients = this.clients.filter((c) => c.id !== client.id);
        this.users = this.users.filter(user => user.id !== client.id);
        console.log('Client disconnected:', client.id);
        console.log('Current Clients', this.users);
        this.server.emit("activated", this.users)
    }

    @SubscribeMessage('chat')
    async handleMessage(@MessageBody() payload: any): Promise<void>  {
        const body = payload.body;
        const {data} = await axios.post('http://127.0.0.1:5000/test', {body});
        this.server.emit('chat', {sender: payload.sender, body: data});
    }

    @SubscribeMessage('user')
    handleNickname(@MessageBody() payload: any): void {
        console.log(payload);
        this.users.push({id: payload.id, nickname: payload.nickname})
        console.log('Current Clients', this.users);
        this.server.emit("activated", this.users)
    }
}
  