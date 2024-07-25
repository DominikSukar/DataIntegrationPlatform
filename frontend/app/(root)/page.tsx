"use client";
import React, { useState } from 'react';

import { ProfileForm } from "@/components/Form"

interface Match {
  win: boolean;
  championId: number;
  championName: string;
  invidualPosition: string;
  teamId: number;
}

const Home = () => {
  const [matchHistory, setMatchHistory] = useState<Match[]|null>(null)

  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <div className="text-7xl m-6 backdrop-blur-md backdrop-brightness-75 select-none">FF15.GG</div>
      <ProfileForm setMatchHistory={setMatchHistory}></ProfileForm>
    </main>
  )
}

export default Home