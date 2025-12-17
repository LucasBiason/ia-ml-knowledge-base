/**
 * Main chat page.
 */
'use client';

import { useState } from 'react';
import ChatInterface from '@/components/ChatInterface';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-8">
      <div className="w-full max-w-4xl">
        <h1 className="text-3xl font-bold mb-8 text-center">
          Chat Multimodal
        </h1>
        <ChatInterface />
      </div>
    </main>
  );
}





