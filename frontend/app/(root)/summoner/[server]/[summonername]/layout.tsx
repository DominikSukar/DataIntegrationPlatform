import Logo from "@/components/game/Logo"
import Link from "next/link"

export default function DashboardLayout({
    children,
  }: {
    children: React.ReactNode
  }) {
    return (
      <section>
        <nav></nav>
        <Link href="/">
            <div className="absolute 0">
                <Logo></Logo>
            </div>
        </Link>
        {children}
      </section>
    )
  }