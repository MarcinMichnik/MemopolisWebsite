import React from 'react';

import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

const CustomLayout = (props) => {
    return     <>
    <Layout>
      <Header>Header</Header>
      <Layout>
        <Content>{props.children}</Content>
        <Sider>Sider</Sider>
      </Layout>
      <Footer>Footer</Footer>
    </Layout>
  </>
}

export default CustomLayout;