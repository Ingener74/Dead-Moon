
ListItem = React.createClass
    render: ->
        <button type="button" className="list-group-item">{@props.title}</button>

List = React.createClass
    componentDidMount: ->
        $.post '/explore/current', ((data)->
            @setState items:data.content.map (item)->
                link: "/explore/" + item
                title: item
            ).bind this
    getInitialState: ->
        items: []
    handleClick: (index)->
        console.log index
    render: ->
        <div className="list-group">
            {@state.items.map ((item, index)->
                <ListItem title={item.title} onClick={@handleClick.bind this, index} />).bind this
            }
        </div>


React.render <List />, document.getElementById("explore-list")
