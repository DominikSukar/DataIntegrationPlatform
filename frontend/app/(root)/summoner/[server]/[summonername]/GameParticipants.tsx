import GameParticipantsSingle from "./GameParticipantsSingle";
import { Participant, Info } from "@/types/matchTypes";

export default async function GameParticipants({
  team_1,
  team_2,
  info,
}: {
  team_1: Participant[];
  team_2: Participant[];
  info: Info;
}) {
  return (
    <div className="flex justify-center items-center invisible w-0 xl:visible xl:w-max">
      <div>
        {team_1.map((participant, index) => (
          <GameParticipantsSingle key={index} participant={participant} info={info} />
        ))}
      </div>
      <div>
        {team_2.map((participant, index) => (
          <GameParticipantsSingle key={index} participant={participant} info={info} />
        ))}
      </div>
    </div>
  );
}
