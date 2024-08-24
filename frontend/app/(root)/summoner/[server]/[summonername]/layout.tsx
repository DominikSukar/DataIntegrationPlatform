import Logo from "@/components/game/Logo";
import Link from "next/link";

import SummonersAnimationWrapper from "@/components/animationWrappers/Summoners";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <section>
      <nav></nav>
      <Link href="/">
        <div className="absolute 0">
          <Logo></Logo>
        </div>
      </Link>
      <SummonersAnimationWrapper>{children}</SummonersAnimationWrapper>
    </section>
  );
}