import Link from 'next/link';
import ChampionIcon from '../components/ChampionIcon'

import { Participant, Info } from '@/types/matchTypes';

function MatchParticipant({participant, info}: {participant: Participant, info: Info}) {
  try {
    const server = info.server
    console.log("Server:", server)
  } catch (err) {
    console.log("Participant:")
  }

  if (participant.teamId === 100) {
    return (
      <div className="flex font-light text-xs justify-end items-center">
          <Link href={`/summoner/${info.server}/${participant.summonerName}_${participant.tagLine}`}
          className="no-underline">
            <div className="w-28 text-right overflow-hidden whitespace-nowrap text-ellipsis text-white">{participant.summonerName}#{participant.tagLine}</div>
          </Link> 
          <ChampionIcon championName={participant.championName}></ChampionIcon>
          <div className="w-16 flex justify-center items-center">{participant.kills}{<span className="text-slate-400">/</span>}{<span className="text-red-600 font-bold">{participant.deaths}</span>}{<span className="text-slate-400">/</span>}{participant.assists}</div>
      </div>
    )
  }

  return (
    <div className="flex font-light text-xs justify-start items-center">
        <div className="w-16 flex justify-center items-center">{participant.kills}{<span className="text-slate-400">/</span>}{<span className="text-red-600 font-bold">{participant.deaths}</span>}{<span className="text-slate-400">/</span>}{participant.assists}</div>
        <ChampionIcon championName={participant.championName}></ChampionIcon>
        <Link href={`/summoner/${participant.server}/${participant.summonerName}_${participant.tagLine}`}
        className="no-underline">
          <div className="w-28 text-left overflow-hidden whitespace-nowrap text-ellipsis text-white">{participant.summonerName}#{participant.tagLine}</div>
        </Link> 
    </div>
  )
}

export default MatchParticipant