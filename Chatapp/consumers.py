import json
from channels.generic.websocket import AsyncWebsocketConsumer

# Store waiting users by interest
waiting_users = {}

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.interest = self.scope['url_route']['kwargs']['interest']
        await self.accept()

        # Match users based on interest
        if self.interest in waiting_users and waiting_users[self.interest]:
            self.partner = waiting_users[self.interest].pop(0)  # Pair with the first waiting user
            self.partner.partner = self
            await self.partner.send(text_data=json.dumps({"message": "Connected to someone with the same interest!"}))
            await self.send(text_data=json.dumps({"message": "Connected to someone with the same interest!"}))
        else:
            self.partner = None
            if self.interest not in waiting_users:
                waiting_users[self.interest] = []
            waiting_users[self.interest].append(self)

    async def disconnect(self, close_code):
        if self.interest in waiting_users and self in waiting_users[self.interest]:
            waiting_users[self.interest].remove(self)
        if self.partner:
            await self.partner.send(text_data=json.dumps({"message": "Your partner has disconnected."}))
            self.partner.partner = None

    async def receive(self, text_data):
        if self.partner:
            await self.partner.send(text_data=text_data)  # Forward message
