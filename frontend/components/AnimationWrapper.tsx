'use client';

import { motion, AnimatePresence } from 'framer-motion';
import { usePathname } from 'next/navigation';

const variants = {
  hidden: { opacity: 0, y: 50, scale: 0.95 },
  enter: { opacity: 1, y: 0, scale: 1 },
  exit: { opacity: 0, y: -50, scale: 0.95 },
};

export default function AnimationWrapper({
  children,
}: {
  children: React.ReactNode
}) {
  const pathname = usePathname();

  return (
    <AnimatePresence mode="wait">
      <motion.main
        key={pathname}
        variants={variants}
        initial="hidden"
        animate="enter"
        exit="exit"
        transition={{ type: 'linear' }}
      >
        {children}
      </motion.main>
    </AnimatePresence>
  );
}