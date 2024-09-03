'use client';

import React, { useState, ReactNode } from 'react';

interface CSButtonProps {
  children: (isVisible: boolean) => ReactNode;
}

export default function CSButton({ children }: CSButtonProps) {
  const [isVisible, setIsVisible] = useState<boolean>(false);

  return (
    <>
      <button onClick={() => setIsVisible(!isVisible)}>
        {isVisible ? 'Hide' : 'Show'} Content
      </button>
      {children(isVisible)}
    </>
  );
}