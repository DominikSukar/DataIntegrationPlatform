import Logo from "@/components/Logo";
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
        <div className="text-center lg:absolute 0">
          <Logo></Logo>
        </div>
      </Link>
      <SummonersAnimationWrapper>{children}</SummonersAnimationWrapper>
    </section>
  );
}
