import fastify from 'fastify'

const server = fastify()

const TEMPERATURE_API_URL = process.env.TEMPERATURE_API_URL ?? "http://127.0.0.1:8081"

server.get<{Params: {id: string}}>('/api/v2/telemetry/sensors/:id', async (request, reply) => {

  const temperature =  await fetch(`${TEMPERATURE_API_URL}/temperature/${request.params.id}`).then(resp => resp.json())

  return JSON.stringify(temperature)
})

server.listen({ host: "0.0.0.0", port: 8080 }, (err, address) => {
  if (err) {
    console.error(err)
    process.exit(1)
  }
  console.log(`Server listening at ${address}`)
})