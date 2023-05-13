import React, { useState } from 'react';
import { Nav, Tab, TabContent } from 'react-bootstrap'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faEnvelope, faUser } from '@fortawesome/free-solid-svg-icons';

import ProfileUser from './ProfileUser'
import Recommandation2 from './Recommandation2'
import Recommandation1 from './Recommandation1'
import Blog from './BlogPost'



const HorizontalMenu = () => {

  const [activeTab, setActiveTab] = useState('tab1');

  const handleTabSelect = (tab) => {
    setActiveTab(tab);
  }

  return (
      <Tab.Container activeKey={activeTab} onSelect={handleTabSelect} className="horizontal-menu">
        <Nav variant="pills" className="horizontal-menu">
          <Nav.Item>
            <Nav.Link eventKey="tab1"><FontAwesomeIcon icon={faHome} /> Profile</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="tab2"><FontAwesomeIcon icon={faUser} /> Blog</Nav.Link>
          </Nav.Item>
        </Nav>
        <TabContent>
          <Tab.Pane eventKey="tab1">
            <ProfileUser/>
          </Tab.Pane>
          <Tab.Pane eventKey="tab2" >
            <Blog/>
          </Tab.Pane>
        </TabContent>
      </Tab.Container>
    
  );
};

export default HorizontalMenu;








