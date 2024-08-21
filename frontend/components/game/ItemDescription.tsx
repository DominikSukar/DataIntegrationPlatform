"use client"
import React from 'react';
import styled from 'styled-components';

const StyledDescription = styled.div`
  .mainText {
    margin-bottom: 10px;
  }

  .stats {
    display: inline;
  }

  .status {
    display: inline;
  }

  .attention {
    color: #ffd700;
    font-weight: bold;
    margin-right: 5px;
  }

  .keyword, .keywordStealth {
    color: #800080;
    font-style: italic;
  }

  .active, .unique, .passive {
    color: #00ff00;
    font-weight: bold;
  }

  .rarityGeneric, .rarityLegendary, .rarityMythic {
    color: #3b82f6;
    font-weight: bold;
  }

  .rules {
    color: #3b82f6;
    font-weight: bold;
    margin-top: 10px;
    display: block;
  }

  .li {
    color: #3b82f6;
    font-weight: bold;
    margin-left: 20px;
  }

  p, br {
    display: block;
    margin: 0;
    padding: 0;
  }

  p {
    margin-bottom: 10px;
  }

  br + br {
    margin-bottom: 10px;
  }
`;


const customElements = {
  mainText: 'mainText',
  stats: 'stats',
  status: 'status',
  attention: 'attention',
  keyword: 'keyword',
  li: 'li',
  rarityMythic: 'rarityMythic',
  rarityLegendary: 'rarityLegendary',
  rarityGeneric: 'rarityGeneric',
  keywordStealth: 'keywordStealth',
  active: 'active',
  unique: 'unique',
  passive: 'passive',
  rules: 'rules',
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