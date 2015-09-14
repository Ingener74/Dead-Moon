Title = React.createClass
    componentDidMount: ->
        $.post '/test/title', ((data)->
            @setState title: data.title).bind this
    getInitialState: ->
        title: "initial state"
    render: ->
        <div>
            <h2>Title : {this.state.title}, title from props: {this.props.title2}</h2>
        </div>

Submitter = React.createClass
    getInitialState: ->
        return title: "initial"
    handleClick: (event)->
        $.post '/test/button', ((data)->
                @setState title: data.title).bind this
    render: ->
        <div>
            <Title title2={this.state.title}/>
            <button onClick=@handleClick type="button" className="btn btn-success">Submit</button>
        </div>

SubmittedTitle = React.createClass
    render: ->
        <div>
            <Submitter />
        </div>

React.render <SubmittedTitle />, document.getElementById('content')