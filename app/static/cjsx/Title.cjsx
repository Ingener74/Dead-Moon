Title = React.createClass
    render: ->
        <div>
            <h2>Title: {@props.title}</h2>
        </div>

Submitter = React.createClass
    render: ->
        <div>
            <button onClick={@props.onClick} className="btn btn-warning">Click me</button>
        </div>

SubmittedTitle = React.createClass
    getInitialState: ->
        return title: ""
    render: ->
        <div>
            <Title title={@state.title}/>
            <Submitter onClick={@handleClick}/>
        </div>
    handleClick: ->
        $.post '/test/button', ((data)->
            @setState title: data.title).bind this

React.render <SubmittedTitle />, document.getElementById('content')