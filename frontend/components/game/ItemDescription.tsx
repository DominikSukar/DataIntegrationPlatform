"use client"
import React from 'react';
import styled from 'styled-components'; // Or use your preferred CSS-in-JS solution

const StyledDescription = styled.div`
  .mainText {}
  
  .stats {
    display: inline; /* Inline for stats, to appear on the same line */
  }
  
  .attention {
    color: #ffd700; /* Gold color for emphasis */
    font-weight: bold;
  }
  
  .keywordStealth {
    color: #800080; /* Purple for stealth keywords */
    font-style: italic;
  }
  
  .active {
    color: #00ff00; /* Green for active abilities */
    font-weight: bold;
  }
  .passive {
    color: #3b82f6;
    font-weight: bold;
  }    

  p, br {
    display: block;
    margin: 0;
    padding: 0;
  }
`;

const customElements = {
  mainText: 'mainText',
  stats: 'stats',
  attention: 'attention',
  keywordStealth: 'keywordStealth',
  active: 'active',
  passive: 'passive',
  br: 'br',
};

const ItemDescription: React.FC<{ description: string }> = ({ description }) => {
  const parseHTML = (html: string) => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    
    const parseNode = (node: Node): React.ReactNode => {
      if (node.nodeType === Node.TEXT_NODE) {
        return node.textContent;
      }
      
      if (node.nodeType === Node.ELEMENT_NODE) {
        const element = node as Element;
        const tagName = element.tagName.toLowerCase() as keyof typeof customElements;
        const className = customElements[tagName] || '';
        
        const children = Array.from(element.childNodes).map(parseNode);

        if (tagName === 'br') {
          return <br />;
        }
        
        return React.createElement(
          'span',
          { className },
          ...children
        );
      }
      
      return null;
    };
    
    return parseNode(doc.body);
  };

  return <StyledDescription>{parseHTML(description)}</StyledDescription>;
};

export default ItemDescription;