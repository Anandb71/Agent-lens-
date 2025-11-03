<script lang="ts">
  export let data;
  let steps = data.steps || [];

  function getStepColor(stepType: string) {
    switch (stepType) {
      case 'THOUGHT':
        return 'bg-blue-100 border-blue-500';
      case 'TOOL_CALL':
        return 'bg-yellow-100 border-yellow-500';
      case 'OBSERVATION':
        return 'bg-green-100 border-green-500';
      case 'ERROR':
        return 'bg-red-100 border-red-500';
      default:
        return 'bg-gray-100 border-gray-500';
    }
  }
</script>

<div class="min-h-screen bg-gray-50 p-8">
  <div class="max-w-4xl mx-auto">
    <a href="/" class="text-blue-500 hover:underline mb-8 block">&larr; Back to Sessions</a>
    <h1 class="text-3xl font-bold text-gray-900 mb-8">Session Timeline</h1>

    <div class="space-y-4">
      {#if steps.length === 0}
        <p class="text-gray-500">No steps found for this session.</p>
      {:else}
        {#each steps as step (step.id)}
          <div class="p-4 rounded-lg border {getStepColor(step.step_type)}">
            <div class="flex items-center justify-between mb-2">
              <span class="font-bold text-sm uppercase tracking-wider text-gray-700">
                {step.step_type}
              </span>
              <span class="text-xs text-gray-500">Step ID: {step.id}</span>
            </div>
            <pre class="whitespace-pre-wrap font-mono text-sm text-gray-800 bg-white p-3 rounded">{step.content}</pre>
          </div>
        {/each}
      {/if}
    </div>
  </div>
</div>

<style>
  pre {
    font-family: 'Courier New', Courier, monospace;
  }
</style>