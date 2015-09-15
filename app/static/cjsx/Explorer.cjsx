
ListItem = React.createClass
    render: ->
        <button type="button" onClick={@props.onClick} className="list-group-item">{@props.title}</button>

List = React.createClass
    componentDidMount: ->
        $.post '/explore/current', ((data)->
            @setState items:data.content.map (item)->
                title: item
            ).bind this
    getInitialState: ->
        items: []
    render: ->
        <div className="list-group">
            {@state.items.map ((item, index)->
                <ListItem title={item.title} onClick={@handleClick.bind this, index} />).bind this
            }
        </div>
    handleClick: (index)->
        console.log @state.items[index].title
        $.post '/explore/' + @state.items[index].title, ((data)->
            @setState items: data.content.map (item)->
                title: item
            ).bind this

React.render <List />, document.getElementById("explore-list")
