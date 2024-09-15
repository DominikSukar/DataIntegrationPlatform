import Image from "next/image";

import { DOMAIN } from "@/constants/api";

export default async function ProfileIcon({
  iconID,
  size,
}: {
  iconID: number;
  size: number;
}) {
  return (
    <Image
      src={`${DOMAIN}/static/dragontail-14.15.1/14.15.1/img/profileicon/${iconID}.png`}
      className="m-2"
      width={size}
      height={size}
      alt={`Profile icon ${iconID}`}
    />
  );
}
