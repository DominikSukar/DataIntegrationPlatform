import { fetchSummonerData } from "@/api/summoner"
import { PageProps } from "@/types/matchTypes";
import ProfileIcon from "./ProfileIcon";
import RankIcon from "./RankIcon";

const User = async ({ params }: PageProps) => {
  const user = await fetchSummonerData(params);
  return (
    <div className="flex items-center place-content-between min-w-[1000px] text-white border border-white bg-white bg-opacity-20 backdrop-blur-md mb-28 mt-10">
        <div className="flex items-center">
          <ProfileIcon iconID={user.profileIconId} size={120}></ProfileIcon>
          <div className="flex flex-col">
              <h1 className="font-bold m-2">{params.summonerName}</h1>
              <h3 className="font-bold m-2">Level {user.summonerLevel}</h3>
          </div>
        </div>
        <div className="flex  mr-16">
          <RankIcon rankName={user.tier} size={120}></RankIcon>
          <div className="flex flex-col items-center justify-center">
            <div className="flex">
              {user.tier} {user.rank} <div className="text-slate-400 ml-2">{user.leaguePoints} LP</div> 
            </div>
            <div className="flex"><p className="text-green-600">{user.wins}W</p><p className="ml-1 text-red-600">{user.losses}L </p>
              <div className="text-slate-400 ml-2">{user.winrate} % WR</div>
            </div>
            
          </div>
        </div>
    </div>
  )
}

export default User