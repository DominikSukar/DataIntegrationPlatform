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
  timePlayed: number,
  summonerName: string
}

interface matchData {
  main_participant: Participant,
  team_1: Participant[],
  team_2: Participant[],
}

const User = ({searchParams}: {searchParams: {summonername: string, server: string}}) => {
  const summonerName = searchParams.summonername
  const server = searchParams.server

  const [matches, setMatches] = useState<matchData[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://localhost:8000/match_history/?summoner_name=${summonerName}&server=${server}`);
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
  }, [summonerName, server]);

  return (
    <div>
      <div>{summonerName} # {server}</div>
      <div className="flex flex-col items-center">
        {matches.map((match, index) => (
          <Game key={index} match={match}/>
        ))}
      </div>
    </div>
  )
}

export default User