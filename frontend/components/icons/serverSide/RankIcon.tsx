import Image from "next/image";

import { DOMAIN } from "@/constants/api";

/* Component is used on both client and server side. Do not put async.*/
export default function RankIcon({
  rankName,
  size,
}: {
  rankName: string;
  size: number;
}) {
  return (
    <Image
      src={`${DOMAIN}/static/dragontail-14.15.1/14.15.1/img/ranked-emblems/${rankName}.png`}
      className="mx-0.5"
      width={size}
      height={size}
      alt={`Rank icon ${rankName}`}
    />
  );
}
