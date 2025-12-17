/**
 * Main chat interface component.
 */
'use client';

import { useState } from 'react';
import MessageList from './MessageList';
import MessageInput from './MessageInput';
import { Message, ChatSession } from '@/types/chat';

export default function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [session, setSession] = useState<ChatSession | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSendMessage = async (content: string) => {
    // TODO: Implement API call
    console.log('Sending message:', content);
  };

  return (
    <div className="flex flex-col h-[600px] border rounded-lg shadow-lg">
      <div className="flex-1 overflow-y-auto p-4">
        <MessageList messages={messages} />
      </div>
      <div className="border-t p-4">
        <MessageInput onSend={handleSendMessage} disabled={loading} />
      </div>
    </div>
  );
}





