import ChampionIcon from '../components/ChampionIcon'

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
  summonerName: string;
}

function MatchParticipant({participant}: {participant: Participant}) {

  if (participant.teamId === 100) {
    return (
      <div className="flex font-light text-xs justify-end items-center">
          <span>{participant.summonerName}</span>
          <ChampionIcon championName={participant.championName}></ChampionIcon>
          <div className="w-16 flex justify-center items-center">{participant.kills}{<span className="text-slate-400">/</span>}{<span className="text-red-600 font-bold">{participant.deaths}</span>}{<span className="text-slate-400">/</span>}{participant.assists}</div>
      </div>
    )
  }

  return (
    <div className="flex font-light text-xs justify-start items-center">
        <div className="w-16 flex justify-center items-center">{participant.kills}{<span className="text-slate-400">/</span>}{<span className="text-red-600 font-bold">{participant.deaths}</span>}{<span className="text-slate-400">/</span>}{participant.assists}</div>
        <ChampionIcon championName={participant.championName}></ChampionIcon>
        <div>{participant.summonerName}</div>
    </div>
  )
}

export default MatchParticipant