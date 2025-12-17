/**
 * TypeScript types for chat functionality.
 */

export type MessageRole = 'system' | 'user' | 'assistant';
export type MessageType = 'text' | 'image' | 'audio';

export interface Message {
  id: number;
  session_id: number;
  role: MessageRole;
  content: string;
  message_type: MessageType;
  created_at: string;
  metadata?: Record<string, any>;
}

export interface ChatSession {
  id: number;
  user_id: number;
  title: string | null;
  created_at: string;
  updated_at: string | null;
  message_count?: number;
}

export interface ChatRequest {
  message: string;
  session_id?: number;
  stream?: boolean;
  model?: string;
  temperature?: number;
  max_tokens?: number;
}

export interface ChatResponse {
  message: string;
  session_id: number;
  message_id: number;
}

export interface ChatHistory {
  session: ChatSession;
  messages: Message[];
}





