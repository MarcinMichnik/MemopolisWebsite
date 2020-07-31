import React from 'react';
import './App.css';
import 'antd/dist/antd.css';

import CustomLayout from './containers/Layout';
import MemeList from './containers/MemeListView';

function App() {
  return (
    <div className="App">
        <CustomLayout>
          <MemeList />
        </CustomLayout>
    </div>
  );
}

export default App;
