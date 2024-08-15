import { fetchSummonerData } from "@/api/summoner"
import { PageProps } from "@/types/matchTypes";
import ProfileIcon from "./ProfileIcon";

const User = async ({ params }: PageProps) => {
  const user = await fetchSummonerData(params);
  return (
    <div className="flex items-center min-w-[1000px] text-white border border-white bg-white bg-opacity-20 backdrop-blur-md mb-28 mt-10">
        <ProfileIcon iconID={user.profileIconId} size={120}></ProfileIcon>
        <div className="flex flex-col">
            <h1 className="font-bold m-2">{params.summonerName}</h1>
            <h3 className="font-bold m-2">Level {user.summonerLevel}</h3>
        </div>
    </div>
  )
}

export default User