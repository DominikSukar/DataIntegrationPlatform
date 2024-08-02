"use client"
import { useEffect, useState } from 'react';

import Game  from "@/components/Game"

interface matchData {
  win: boolean;
  championId: number;
  championName: string;
  individualPosition: string;
  teamId: number;
}

const User = ({searchParams}: {searchParams: {summonername: string, tag: string}}) => {
  const summonerName = searchParams.summonername
  const tag = searchParams.tag

  const [matches, setMatches] = useState<matchData[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://localhost:8000/match_history?nickname=${summonerName}&tag=${tag}`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data: matchData[] = await response.json();
        setMatches(data);
      } catch (error) {
        console.error('Fetch error:', error);
      }
    };

    fetchData();
  }, [summonerName, tag]);

  return (
    <div>
      <div>{summonerName} # {tag}</div>
      {matches.map((match, index) => (
        <Game key={index} match={match}/>
      ))}
    </div>
  )
}

export default User