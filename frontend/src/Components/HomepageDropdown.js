import { useState, useContext } from "react";
import { HomeScreenContext } from "../Context/HomeScreenContext";
import { Nav, Tab } from "react-bootstrap";

import { clearBookList } from "../Actions/bookActions";
import { useDispatch } from "react-redux";

function TabsExample() {
    const dispatch = useDispatch();
    const [activeTab, setActiveTab] = useState("tab1");
    const { handleSearchType, setSearchValue } = useContext(HomeScreenContext);
    const handleTabSelect = (tab) => {
        dispatch(clearBookList());
        setSearchValue('');
        setActiveTab(tab);
        handleSearchType(tab);
    };

    return (
        <Tab.Container activeKey={activeTab} onSelect={handleTabSelect}>
            <Nav variant="pills">
                <Nav.Item>
                    <Nav.Link eventKey="tab1">Latest Books</Nav.Link>
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
