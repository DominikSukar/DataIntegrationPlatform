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
      <div className="fixed z-50">
        <nav>
          <Link href="/">
            <div className="text-center">
              <Logo></Logo>
            </div>
          </Link>
        </nav>
      </div>
      <SummonersAnimationWrapper>{children}</SummonersAnimationWrapper>
      <footer className="text-white py-4 text-center">
        <p>&copy; 2024 FF15. All rights reserved.</p>
      </footer>
    </section>
  );
}
