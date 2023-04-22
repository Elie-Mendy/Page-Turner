import React, { useState } from 'react';
import { Nav, Tab } from 'react-bootstrap';

function TabsExample() {
  const [activeTab, setActiveTab] = useState('tab1');

  const handleTabSelect = (tab) => {
    setActiveTab(tab);
  }

  return (
    <Tab.Container activeKey={activeTab} onSelect={handleTabSelect}>
      <Nav variant="pills">
        <Nav.Item>
          <Nav.Link eventKey="tab1">Latest books</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="tab2">Recommandation 1</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="tab3">Recommandation 2</Nav.Link>
        </Nav.Item>
      </Nav>
    </Tab.Container>
  );
}

export default TabsExample;