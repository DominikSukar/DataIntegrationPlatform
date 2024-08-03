"use client"
import { useEffect, useState } from 'react';

import Game  from "@/components/Game"

interface Participant {
  win: boolean;
  championId: number;
  championName: string;
  individualPosition: string;
  teamId: number;
  kills: number,
  deaths: number,
  assists: number,
  timePlayed: number
}

interface matchData {
  main_participant: Participant,
  team_1: Participant[],
  team_2: Participant[],
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
      <div className="flex flex-col items-center">
        {matches.map((match, index) => (
          <Game key={index} match={match}/>
        ))}
      </div>
    </div>
  )
}

export default User