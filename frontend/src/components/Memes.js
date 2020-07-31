import React from 'react';
import { List, Avatar, Space } from 'antd';
import { MessageOutlined, LikeOutlined} from '@ant-design/icons';




const IconText = ({ icon, text }) => (
  <Space>
    {React.createElement(icon)}
    {text}
  </Space>
);

const Memes = (props) => {
    return (
        <List
        itemLayout="vertical"
        size="large"
        pagination={{
          onChange: page => {
            console.log(page);
          },
          pageSize: 10,
        }}
        dataSource={props.data}
        renderItem={item => (
          <List.Item
            key={item.title}
            actions={[
              <IconText icon={LikeOutlined} text={item.num_vote_up} key="list-vertical-like-o" />,
              <IconText icon={MessageOutlined} text="Komentarze" key="list-vertical-message" />,
            ]}
          >
            <List.Item.Meta
              title={<a href={item.href}>{item.title}</a>}

            />
              <img
                width={400}
                alt="logo"
                src={item.image}
              />
          </List.Item>
        )}
      />
    
    )
}



export default Memes;