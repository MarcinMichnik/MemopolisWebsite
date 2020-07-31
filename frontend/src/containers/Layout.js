import React from 'react';

import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

const CustomLayout = (props) => {
    return     <>
    <Layout>
      <Header>Memopolis</Header>
      <Layout>
        <Content>{props.children}</Content>
        <Sider>Top</Sider>
      </Layout>
      <Footer>Memopolis &copy;</Footer>
    </Layout>
  </>
}

export default CustomLayout;