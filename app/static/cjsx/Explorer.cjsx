
ListItem = React.createClass
    render: ->
        <a href={@props.link} className="list-group-item">{@props.title}</a>

List = React.createClass
    render: ->
        <div className="list-group">
            {@props.items.map (item)->
                console.log item
                return <ListItem link=item.link title=item.title />
            }
        </div>

React.render <List items ={[
        link: "link-0"
        title: "link-title-0",
        link: "link-1"
        title: "link-title-1",
        link: "link-2"
        title: "link-title-2"
    ]}/>, document.getElementById("explore-list")
