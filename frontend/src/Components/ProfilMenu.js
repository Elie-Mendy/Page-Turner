import React, { useState } from 'react';
import { Nav, Tab } from 'react-bootstrap'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faEnvelope, faUser } from '@fortawesome/free-solid-svg-icons';

const HorizontalMenu = () => {

  const [activeTab, setActiveTab] = useState('tab1');

  const handleTabSelect = (tab) => {
    setActiveTab(tab);
  }

  return (
    <Tab.Container activeKey={activeTab} onSelect={handleTabSelect} className="horizontal-menu">
      <Nav variant="pills" className="horizontal-menu">
        <Nav.Item>
          <Nav.Link eventKey="tab1"><FontAwesomeIcon icon={faHome} /> Latest books</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="tab2"><FontAwesomeIcon icon={faEnvelope} /> Recommandation 1</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="tab3"><FontAwesomeIcon icon={faUser} /> Recommandation 2</Nav.Link>
        </Nav.Item>
      </Nav>
    </Tab.Container>
  );
};

export default HorizontalMenu;