Title = React.createClass
  render: ->
    <div>
      <h2>Title: </h2>
    </div>

React.render React.createElement(Title, null), document.getElementById('react_content')