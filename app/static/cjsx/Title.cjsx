Title = React.createClass
    getInitialState: ->
        title: "My Title"
    render: ->
        <div>
            <h2>Title : {this.state.title}, title from props: {this.props.title2}</h2>
        </div>

Submitter = React.createClass
    render: ->
        <button type="button" class="btn btn-default">Submit</button>

SubmittedTitle = React.createClass
    render: ->
        <div>
            <Title title2="prop title 2"/>
            <Submitter />
        </div>

React.render <SubmittedTitle />, document.getElementById('content')