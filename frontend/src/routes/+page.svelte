<script lang="ts">
	export let data;
	let sessions = data.sessions || [];
</script>

<h1>Agent-Lens Sessions</h1>

{#each sessions as session (session.id)}
  <a href="/session/{session.id}">
    <div class="session-link">
      {session.name} (ID: {session.id})
    </div>
  </a>
{/each}

<style>
  .session-link {
    display: block;
    padding: 10px;
    border: 1px solid #444;
    margin: 5px 0;
    border-radius: 5px;
    text-decoration: none;
    color: white;
  }
  .session-link:hover {
    background-color: #333;
  }
</style>
