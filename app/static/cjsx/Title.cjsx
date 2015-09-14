Title = React.createClass
    componentDidMount: ->
        $.ajax
            url: '/test/title'
            type: 'POST'
            dataType: 'json'
            success: ((data)->
                @setState title: data.title)
                .bind this
            error: ((xhr, status, err)->
                console.log status, err
                .bind this)
    getInitialState: ->
        title: "My Title"
    render: ->
        <div>
            <h2>Title : {this.state.title}, title from props: {this.props.title2}</h2>
        </div>

Submitter = React.createClass
    getInitialState: ->
        return title: "initial"
    handleClick: (event)->
        $.ajax
            url: '/test/button'
            type: 'POST'
            dataType: 'json'
            success: ((data)->
                @setState title: data.title)
                .bind this
            error: ((xhr, status, err)->
                alert status, err)
                .bind this

    render: ->
        <div>
            <Title title2={this.state.title}/>
            <button onClick=@handleClick type="button" class="btn btn-default">Submit</button>
        </div>

SubmittedTitle = React.createClass
    render: ->
        <div>
            <Submitter />
        </div>

React.render <SubmittedTitle />, document.getElementById('content')